<script>
    import * as d3 from "d3";
    import VisualizationWrapper from "./VisualizationWrapper.svelte";
    import { onMount } from "svelte/internal";

    export let cssHeight;
    export let cssWidth;
    export let data;
    export let Title = "";

    let paddings = {
        top: 50
    }

    let data2;
    let fig_size;

    let width = 0;
    let height = 0;

    let g;

    let filters = [
        "invert(100%)", // white
        "invert(48%) sepia(79%) saturate(2476%) hue-rotate(200deg) brightness(70%) contrast(119%)", // blue
        "invert(48%) sepia(79%) saturate(2476%) hue-rotate(80deg) brightness(70%) contrast(119%)", // green
        "invert(48%) sepia(79%) saturate(3076%) hue-rotate(-10deg) brightness(90%) contrast(119%)", // orange
        "invert(48%) sepia(79%) saturate(2476%) hue-rotate(0deg) brightness(150%) contrast(119%)", // yellow
        "invert(48%) sepia(79%) saturate(2476%) hue-rotate(200deg) brightness(130%) contrast(80%)", // light blue
    ]


    onMount(() => {
        data2 = data.map((d,i) => [...Array(Math.floor(d.value)).keys()].map(e => {
            return {
                id: `${i}-${e}`,
                category: i,
                index: e
            }
        })).flat()

        let links = data.map((d,i) => [...Array(Math.floor(d.value)).keys()].map(e => {
            return {source:`${i}-0`, target:`${i}-${e}`}
        })).flat()

        var node = d3.select(g)
            .selectAll("image")
            .data(data2)
            .enter()
            .append("image")
                .attr("class", "node")
                .attr("xlink:href", "images/human_icon.png")
                .attr("x", (d) => (width / 2))
                .attr("y", d => (height / 2))
                .attr("height", Math.min(width, height)/12)
                .attr("onmouseover", `this.style.opacity=0.7`)
                .attr("onmouseout", "this.style.opacity=1")
                .style("filter", d => filters[d.category])

        fig_size = Math.min(width, height)/12

        var simulation = d3.forceSimulation(data2)
            .force("center", d3.forceCenter().strength(1.0).x(width/2).y(height/2))
            .force("charge", d3.forceManyBody().strength(.2))
            .force("collide", d3.forceCollide().strength(.5).radius(Math.min(width, height)/25).iterations(1))
            .force("link", d3.forceLink().strength(0.6).id(d => d.id))
            .force("bound", () => {data2.forEach(node => {
                node.x = Math.min(width - fig_size, Math.max(0, node.x));
                node.y = Math.min(height - fig_size, Math.max(node.y, paddings.top));
            })})



        simulation
            .nodes(data2)
            .on("tick", (d) => {
                node
                    .attr("x", d => d.x)
                    .attr("y", d => d.y)
            })
            .force("link").links(links)

    })

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
        mousePosition = { x: positionInSVG.x, y: positionInSVG.y }
        computeSelectedValue(mousePosition)
    }
    function removePointer() {
        mousePosition = { x: null, y: null };
        currentHoveredPoint = null;
    }

    function computeSelectedValue(mousePosition) {

        for (let point of data2) {
            let dis = Math.sqrt((mousePosition.x - point.x) ** 2 + (mousePosition.y - point.y) ** 2)
            if (dis < (fig_size/2)) {
                currentHoveredPoint = data[point.category]
                break;
            }
        }
    }


</script>

<div>
    <VisualizationWrapper
        cssHeight={cssHeight}
        cssWidth={cssWidth}
        mousemove={followMouse}
        mouseleave={removePointer}
        bind:chartWidth={width}
        bind:chartHeight={height}
        id={idContainer}
    >
        <g>
            <text
                x={width/2}
                y={paddings.top/2}
                font-size="24"
                fill="#FFFFFF"
            >
                {Title}
            </text>
        </g>
        <g bind:this={g}/>
    </VisualizationWrapper>
    {#if mousePosition.x != null && currentHoveredPoint}
        <div
            class={mousePosition.x === null ? "tooltip-hidden" : "tooltip-visible"}
            style="left: {pageMousePosition.x + 10}px; top: {pageMousePosition.y + 10}px"
        >
            About {currentHoveredPoint.value.toFixed(2)}% of migrants experience violence as a result of {currentHoveredPoint.label}
        </div>
    {/if}
</div>

<style>
    .icon:hover {
        padding: 2vh;
        background-color: aqua;
    }

    .tooltip-hidden {
        visibility: hidden;
        font-family: "Nunito", sans-serif;
        width: 200px;
        position: absolute;
    }

    .tooltip-visible {
        font: 18px sans-serif;
        font-family: "Nunito", sans-serif;
        visibility: visible;
        background-color: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(8px);
        border-radius: 10px;
        width: 200px;
        color: black;
        position: absolute;
        padding: 10px;
    }

</style>