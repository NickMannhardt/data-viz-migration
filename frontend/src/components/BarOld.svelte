<script>
    import * as d3 from "d3";
    import { scaleLinear } from "d3-scale";
    import { onMount } from "svelte";

    export let data = [];
    export let xTitle = "";
    export let yTitle = "";


    let div;

    let chartWidth = 1000;
    let chartHeight = 360;

    onMount( () => {
        chartWidth = div.clientWidth;
        chartHeight = div.clientHeight;

        d3.selectAll('.bar')
            .data(data)
            .transition()
            .duration(2000)
            .attr("height", d => {
                return chartHeight - paddings.bottom - yScale(d.size)
            })
            .attr("y", d => {
                return yScale(d.size)
            })
    })

    const paddings = {
        top: 50,
        left: 150,
        right: 50,
        bottom: 100,
        gap: 5,
    };

    $: xScale = scaleLinear()
        .domain([
            Math.min(...data.map((d) => d.index)),
            Math.max(...data.map((d) => d.index)) + 1,
        ])
        .range([paddings.left, chartWidth - paddings.right]);
    $: yScale = scaleLinear()
        .domain([
            Math.min(...data.map((d) => d.size)),
            Math.max(...data.map((d) => d.size)),
        ])
        .range([chartHeight - paddings.bottom, paddings.top]);

    
    let xTicks = [];
    let yTicks = [];
    let numTicks = 5;
    $: {
        xTicks = [];
        yTicks = [];

        if (data.length > 1) {
            let index_extent = [
                Math.round(Math.min(...data.map((d) => d.index))),
                Math.round(Math.max(...data.map((d) => d.index)) + 1),
            ];

            let index_increment = chartWidth / data.length

            for (let d of data) {
                xTicks.push(d.label);
            }

            // for (
            //     let i = index_extent[0];
            //     i < index_extent[1];
            //     i = i + Math.max(1, index_increment)
            // ) {
            //     xTicks.push(i)
            // }

            let size_extent = [
                Math.round(Math.min(...data.map((d) => d.size))),
                Math.round(Math.max(...data.map((d) => d.size)) + 1),
            ]

            let size_increment = Math.floor(
                (size_extent[1] - size_extent[0]) / numTicks
            )

            for (
                let i = size_extent[0];
                i < size_extent[1];
                i = i + Math.max(1, size_increment)
            ) {
                yTicks.push(i)
            }
        }
    }

    const idContainer = "svg-container-" + Math.random() * 1000000;
    let mousePosition = { x: null, y: null };
    let pageMousePosition = { x: null, y: null };
    let currentHoveredPoint = null;

    function followMouse(event) {
        const svg = document.getElementById(idContainer);
        if (svg === null) return;
        const dim = svg.getBoundingClientRect();
        pageMousePosition = {
            x: event.pageX,
            y: event.pageY,
        };
        const positionInSVG = {
            x: event.clientX - dim.left,
            y: event.clientY - dim.top,
        };
        mousePosition =
            positionInSVG.x > paddings.left &&
            positionInSVG.x < chartWidth - paddings.right &&
            positionInSVG.y > paddings.top &&
            positionInSVG.y < chartHeight - paddings.bottom
                ? { x: positionInSVG.x, y: positionInSVG.y }
                : { x: null, y: null };
    }
    function removePointer() {
        mousePosition = { x: null, y: null };
    }
    function computeSelectedXValue(value) {
        currentHoveredPoint = 
            data[
                data.indexOf(data.filter((d) => xScale(d.index) >= value)[0]) - 1
            ];
        return data.filter((d) => xScale(d.index) >= value)[0].index - 1;
    }

</script>

<div bind:this={div} class="visualization">
    {#if data.length > 1}
        <svg 
            width={chartWidth}
            height={chartHeight}
            on:mousemove={followMouse}
            on:mouseleave={removePointer}
            id={idContainer}
        >
            <g transform="translate({paddings.left}, 0)">
                {#each yTicks as y}
                    <g
                        class="tick"
                        opacity="1"
                        transform="translate(0,{yScale(y)})"
                    >
                        <line stroke="#FFFFFF" x2={chartWidth - paddings.left - paddings.right} />
                        <text 
                            dy="0.32em" 
                            fill="#FFFFFF" 
                            x="-{10}"
                            text-anchor="end"
                        >
                            {y}
                        </text>
                    </g>
                {/each}
                <text
                    x={chartWidth/2}
                    y={chartHeight - paddings.bottom/2}
                    text-anchor="middle"
                    font-size="16"
                    fill="#FFFFFF"
                >
                    {xTitle}
                </text>
                <text
                    transform={`translate(-${paddings.left/2},${chartHeight/2})rotate(-90)`}
                    text-anchor="middle"
                    font-size="16"
                    fill="#FFFFFF"
                >
                    {yTitle}
                </text>
            </g>
            <g>
                {#each data as d, i}
                    <rect
                        x={xScale(data[i].index) + paddings.gap}
                        y={chartHeight - paddings.bottom - yScale(d.size)}
                        height={yScale(d.size)}
                        width={(chartWidth - paddings.left - paddings.right) / data.length - paddings.gap}
                        fill="#FFFFFF"
                        class="bar"
                    />
                {/each}
            </g>
        </svg>
    {:else}
        <p>No data to display</p>
    {/if}
</div>

<style>
    /* .bar {
        animation: draw-rect 2s;
    }

    @keyframes draw-rect {
        from {
            height: 0;
            y: 4000;
        }
        to {
            height: 4000;
            y: 0;
        }
    } */

    .bar:hover {
        fill: #31a693;
    }

    .visualization {
        font: 25px sans-serif;
        /* margin: auto; */
        /* margin-top: 1px; */
        /* text-align: middle; */
        /* flex-grow: 1; */
    }

    .tooltip-hidden {
        visibility: hidden;
        font-family: "Nunito", sans-serif;
        width: 200px;
        position: absolute;
    }

    .tooltip-visible {
        font: 25px sans-serif;
        font-family: "Nunito", sans-serif;
        visibility: visible;
        background-color: #f0dba8;
        border-radius: 10px;
        width: 200px;
        color: black;
        position: absolute;
        padding: 10px;
    }

    .axis {
        stroke-linejoin: round;
        stroke-dasharray: 4400;
        stroke-dashoffset: 0;
    }
    @keyframes draw {
        from {
            stroke-dashoffset: 4400;
        }
        to {
            stroke-dashoffset: 0;
        }
    }

</style>