<template>
	<el-main>
		<el-alert title="本图数据来源于GitHub开源仓库，经过大量清洗操作后展示！" type="success" style="margin-bottom:20px;"></el-alert>
		<el-row :gutter="15">
			<el-col :lg="24">
				<el-card shadow="never">
					<scEcharts height="1200px" :option="option"></scEcharts>
				</el-card>
			</el-col>
		</el-row>
	</el-main>
</template>

<script>
	import scEcharts from '@/components/scEcharts';

	/**
	 * 引入组件 @/components/scEcharts
	 * 组件内部会自动加载主题 @/components/scEcharts/echarts-theme-T.js
	 * 支持props包括 height，width，option
	 * 组件export百度Echarts所有方法，使用方式: new scEcharts[fun]
	 */

	export default {
		name: 'autocode-methodtoken',
		components: {
			scEcharts
		},
		data() {
			return {
				option: {
					title: {
						text: "Graph Basic",
						subtext: "轻触图中结点获取更多信息",
					},
					tooltip: {
						triggerOn: 'click', // 触发时机
						confine: false, // 是否将 tooltip 框限制在图表的区域内。
						extraCssText: 'box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);', // 额外附加到浮层的 css 样式
						position: ['30%', '10%'],
						formatter: function (x) {
        					return "<p style='white-space: pre-line;'>"+x.data.desc+"</p>" //设置提示框的内容和格式 节点和边都显示name属性
    					}
					}, //提示框
					animationDurationUpdate: 1500,
					animationEasingUpdate: "quinticInOut",
					series: [
					{
						type: "graph",
						layout: "force",
						// symbolSize: 50, //倘若该属性不在link里，则其表示节点的大小；否则即为线两端标记的大小
						symbolSize: (value, params) => {
							switch (params.data.category) {
								case 0:
									return 100;
								case 1:
									return 65;
							}
						},
						roam: true, //鼠标缩放功能
						label: {
							show: true, //是否显示标签
						},
						focusNodeAdjacency: true, //鼠标移到节点上时突出显示结点以及邻节点和边
						edgeSymbol: ["none", "arrow"], //关系两边的展现形式，也即图中线两端的展现形式。arrow为箭头
						edgeSymbolSize: [4, 10],
						draggable: true,
						edgeLabel: {
							fontSize: 20, //关系（也即线）上的标签字体大小
						},
						force: {
							repulsion: 200,
							edgeLength: 120,
						},
						data: this.$TOOL.data.get('STEP2_DATA'),
						// links: [],
						links: this.$TOOL.data.get('STEP1_LINK'),
						lineStyle: {
							opacity: 0.9,
							width: 2,
							curveness: 0,
						},
					},
					]

				}	
			}
		},
	}
</script>

<style>
</style>
