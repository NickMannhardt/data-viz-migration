<script>
    import VisualizationWrapper from "./VisualizationWrapper.svelte";
    import { scaleLinear } from 'd3-scale';

    export let cssHeight;
    export let cssWidth;
    export let data;

    let height = 500;
    let width = 1000;

	$: xScale = scaleLinear()
        .domain([
            0,
            Math.max(...data.map((d) => d.x)) + 1,
        ])
		.range([padding.left, width - padding.right]);

	$: yScale = scaleLinear()
        .domain([
            0,
            Math.max(...data.map((d) => d.y)),
        ])
		.range([height - padding.bottom, padding.top]);

    let xTicks = [];
    let yTicks = [];
    let numTicks = 4;
    $: {
        xTicks = [0];
        yTicks = [0];

        if (data.length > 1) {
            let index_extent = [
                Math.round(Math.min(...data.map((d) => d.x))),
                Math.round(Math.max(...data.map((d) => d.x)) + 1),
            ];

            let index_increment = (index_extent[1] - index_extent[0]) / numTicks

            for (
                let i = index_increment; 
                i < index_extent[1];
                i = i + Math.max(1, index_increment)
            ) {
                xTicks.push(i);
            }

            let size_extent = [
                Math.round(Math.min(...data.map((d) => d.y))),
                Math.round(Math.max(...data.map((d) => d.y)) + 1),
            ]

            let size_increment = Math.floor(
                (size_extent[1] - size_extent[0]) / numTicks
            )

            for (
                let i = size_increment;
                i < size_extent[1];
                i = i + Math.max(1, size_increment)
            ) {
                yTicks.push(i)
            }
        }
    }

	const padding = { top: 20, right: 40, bottom: 40, left: 25 };

</script>

<VisualizationWrapper
    cssHeight={cssHeight}
    cssWidth={cssWidth}
    bind:chartWidth={width}
    bind:chartHeight={height}
>
    <!-- y axis -->
    <g class='axis y-axis'>
        {#each yTicks as tick}
            <g class='tick tick-{tick}' transform='translate(0, {yScale(tick)})'>
                <line x1='{padding.left}' x2='{xScale(22)}'/>
                <text x='{padding.left - 8}' y='+4'>{tick}</text>
            </g>
        {/each}
    </g>

    <!-- x axis -->
    <g class='axis x-axis'>
        {#each xTicks as tick}
            <g class='tick' transform='translate({xScale(tick)},0)'>
                <line y1='{yScale(0)}' y2='{yScale(13)}'/>
                <text y='{height - padding.bottom + 16}'>{tick}</text>
            </g>
        {/each}
    </g>

    <!-- data -->
    {#each data as datum}
        <circle cx='{xScale(datum.x)}' cy='{yScale(datum.y)}' r='5'/>
    {/each}
</VisualizationWrapper>

<style>

	circle {
		fill: orange;
		fill-opacity: 0.6;
		stroke: white;
	}

	.tick line {
		stroke: #ddd;
		stroke-dasharray: 2;
	}

	text {
		font-size: 12px;
		fill: #999;
	}

	.x-axis text {
		text-anchor: middle;
	}

	.y-axis text {
		text-anchor: end;
	}
</style>