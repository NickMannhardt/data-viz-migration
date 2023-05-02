<script>
    import * as d3 from "d3";
    import VisualizationWrapper from "./VisualizationWrapper.svelte";
    import { onMount } from "svelte/internal";

    export let cssHeight;
    export let cssWidth;
    export let data;
    export let xTitle = "";
    export let yTitle = "";

    let width = 0;
    let height = 0;

    let g;

    // let data2 = data.map(d => [...Array(d.size).keys()]).flat().map(d => {a: d})
    // let data2 = data.map(d => [...Array(d.size).keys()])


    onMount(() => {
        let data2 = data.map((d,i) => [...Array(d.size).keys()].map(e => {
            return {
                category: i,
                index: e
            }
        })).flat()
        // let data2 = data.map(d => {return {size: d.size}})

        let white_filter = "invert(100%)"
        let blue_filter = "invert(48%) sepia(79%) saturate(2476%) hue-rotate(200deg) brightness(70%) contrast(119%)"

        var node = d3.select(g)
            .selectAll("image")
            .data(data2)
            // .data(data)
            // .data([...Array(data[0].size).keys()])
            .enter()
            .append("image")
                .attr("class", "node")
                .attr("xlink:href", "/components/human_icon.png")
                .attr("x", (d) => (width / 2 + d.category*40))
                .attr("y", d => (height / 2 + d.category*20))
                .attr("height", Math.min(width, height)/12)
                .style("fill", "white")
                // .style("opacity", 0.5)
                .style("filter", d => d.category == 0 ? white_filter : blue_filter)
                // .style("fill", d => d.category == 0 ? "red" : "blue")
        
        var simulation = d3.forceSimulation()
            .force("center", d3.forceCenter().x(width/2).y(height/2))
            .force("charge", d3.forceManyBody().strength(.1))
            .force("collide", d3.forceCollide().strength(.5).radius(Math.min(width, height)/25).iterations(1))

        simulation
            .nodes(data2)
            .on("tick", (d) => {
                node
                    .attr("x", d => d.x)
                    .attr("y", d => d.y)
            })

    })


</script>

<VisualizationWrapper
    cssHeight={cssHeight}
    cssWidth={cssWidth}
    bind:chartWidth={width}
    bind:chartHeight={height}
>
    <g bind:this={g}/>
</VisualizationWrapper>

<style>
</style>