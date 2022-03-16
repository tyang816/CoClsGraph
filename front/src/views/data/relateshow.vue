<template>
	<el-main>
		<el-alert title="请先初始化仓库，当出现`初始化成功`提示后点击刷新页面！这里只递归搜索了很小一部分数据展示，即使如此若稍有卡顿或只有一条数据，说明数据还在读取或没有索引到信息（因为索引范围小），重新初始化再刷新即可~" type="success" style="margin-bottom:20px;">
			<el-button type="primary" @click="init">初始化一个仓库</el-button>
			<el-button type="primary" @click="refresh">刷新页面</el-button>
		</el-alert>
		<el-row :gutter="15">
			<el-col :lg="24">
				<el-card shadow="never">
					<scEcharts height="600px" :option="option"></scEcharts>
				</el-card>
			</el-col>
		</el-row>
	</el-main>
</template>
 
<script>
	import scEcharts from '@/components/scEcharts';
	import useTabs from '@/utils/useTabs'
	import { ElNotification } from 'element-plus';

	/**
	 * 引入组件 @/components/scEcharts
	 * 组件内部会自动加载主题 @/components/scEcharts/echarts-theme-T.js
	 * 支持props包括 height，width，option
	 * 组件export百度Echarts所有方法，使用方式: new scEcharts[fun]
	 */

	export default {
		name: 'relateshow',
		components: {
			scEcharts,
		},
		data() {
			return {
				option: {
					title: {
						text: '一个仓库的关系图',
						subtext: '关系图可以拖动查看~',
					},
					tooltip: {},
					series: [
					{
						name: '仓库关系图',
						type: 'graph',
						layout: 'force',
						label: {
							show: true,
							position: 'right',
							formatter: '{b}'
						},
						draggable: true,
						scaleLimit: {
							min: 0.4,
							max: 2
						},
						force: {
							edgeLength: 5,
							repulsion: 350,
							gravity: 0.1
						},
						data: this.$TOOL.data.get("NODES"),
						edges: this.$TOOL.data.get("LINKS"),
						categories: this.$TOOL.data.get("CATEGORIES")
					}
					]
				}
			}
		},
		methods: {
			async init(){
				this.$TOOL.data.remove("NODES")
				this.$TOOL.data.remove("LINKS")
				this.$TOOL.data.remove("CATEGORIES")
				this.$TOOL.data.remove("TYPE")
				var number = Math.round(Math.random()*499)+1
				while(number==324||number==110||number==132||number==391||number==315||number==223||number==101){
					number = Math.round(Math.random()*499)+1
				}
				var query = {
					"rep_id": number
				}
				console.log(number)
				var data = await this.$API.test.relateshow.post(query)
				console.log(data)
				var nodes = data.nodes
				var links = data.links
				var categories = data.links
				var type = data.type
				this.$TOOL.data.set("NODES", nodes)
				this.$TOOL.data.set("LINKS", links)
				this.$TOOL.data.set("CATEGORIES", categories)
				this.$TOOL.data.set("TYPE", type)
				ElNotification.success({
					title: '初始化',
					message: '初始化成功！请刷新页面',
				})
			},
			refresh() {
				useTabs.refresh()
			}
		},
	}
</script>

<style>
</style>
