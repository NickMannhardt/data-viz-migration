<script>
    import * as d3 from "d3";
    import { onMount } from "svelte";
    import VisualizationWrapper from "./VisualizationWrapper.svelte";
    import { scaleLinear } from "d3-scale";

    export let cssHeight;
    export let cssWidth;
    export let data;
    export let xTitle = "";
    export let yTitle = "";

    let height = 500;
    let width = 1000;

    const paddings = {
        top: 50,
        left: 150,
        right: 50,
        bottom: 100,
        gap: 5,
    };

    $: xScale = scaleLinear()
        .domain([
            // Math.min(...data.map((d) => d.index)),
            0,
            Math.max(...data.map((d) => d.index)) + 1,
        ])
        .range([paddings.left, width - paddings.right]);
    $: yScale = scaleLinear()
        .domain([
            // Math.min(...data.map((d) => d.size)),
            0,
            Math.max(...data.map((d) => d.size)),
        ])
        .range([height - paddings.bottom, paddings.top]);

    
    let xTicks = [];
    let yTicks = [];
    let numTicks = 5;
    $: {
        xTicks = [];
        yTicks = [];

        if (data.length > 1) {

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
                0,
                Math.round(Math.max(...data.map((d) => d.size)) + 1),
            ]

            let size_increment = Math.floor(
                (size_extent[1]) / numTicks
            )

            for (
                let i = 0;
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

    onMount(() => {
        d3.selectAll('.bar')
            .data(data)
            .transition()
            .duration(2000)
            .attr("height", d => {
                console.log('hi')
                console.log(d)
                return height - paddings.bottom - yScale(d.size)
            })
            .attr("y", d => {
                return yScale(d.size)
            })
    })
</script>

<VisualizationWrapper
    cssHeight={cssHeight}
    cssWidth={cssWidth}
    bind:chartWidth={width}
    bind:chartHeight={height}
    mousemove={followMouse}
    mouseleave={removePointer}
    id={idContainer}
>
    <g transform="translate({paddings.left}, 0)">
        {#each yTicks as y}
            <g
                class="tick"
                opacity="1"
                transform="translate(0,{yScale(y)})"
            >
                <line stroke="#FFFFFF" x2={width - paddings.left - paddings.right} />
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
            x={width/2}
            y={height - paddings.bottom/2}
            text-anchor="middle"
            font-size="16"
            fill="#FFFFFF"
        >
            {xTitle}
        </text>
        <text
            transform={`translate(-${paddings.left/2},${height/2})rotate(-90)`}
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
                y={height - paddings.bottom}
                height={0}
                width={(width - paddings.left - paddings.right) / data.length - paddings.gap}
                fill="#FFFFFF"
                class="bar"
            />
        {/each}
    </g>
</VisualizationWrapper>


<style>
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