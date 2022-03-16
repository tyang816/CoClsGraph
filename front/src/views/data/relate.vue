<template>
	<el-main>
		<el-alert title="本图显示仓库最终处理的各种关系！" type="success" style="margin-bottom:20px;"></el-alert>
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

	/**
	 * 引入组件 @/components/scEcharts
	 * 组件内部会自动加载主题 @/components/scEcharts/echarts-theme-T.js
	 * 支持props包括 height，width，option
	 * 组件export百度Echarts所有方法，使用方式: new scEcharts[fun]
	 */

	export default {
		name: 'relate',
		components: {
			scEcharts
		},
		data() {
			return {
				option: {
					title: {
						text: '仓库处理的关系图',
						subtext: '圈大小表示重要程度',
					},
					tooltip: {},
					series: [
					{
						name: '仓库关系图',
						type: 'graph',
						layout: 'none',
						roam: true,
						label: {
							show: true,
							position: 'right',
							formatter: '{b}'
						},
						labelLayout: {
							hideOverlap: true
						},
						scaleLimit: {
							min: 0.4,
							max: 2
						},
						lineStyle: {
							color: 'source',
							curveness: 0.3
						},
						data: [
						{
							"id": "0",
							"name": "Repository",
							"symbolSize": 60,
							"x": -400,
							"y": 20,
							"category": 0
						},
						{
							"id": "1",
							"name": "Sourcedir",
							"symbolSize": 30,
							"x": -380,
							"y": 40,
							"category": 1
						},
						{
							"id": "2",
							"name": "Package",
							"symbolSize": 25,
							"x": -390,
							"y": 70,
							"category": 2
						},
						{
							"id": "3",
							"name": "Java",
							"symbolSize": 50,
							"x": -300,
							"y": 60,
							"category": 3
						},
						{
							"id": "4",
							"name": "Import",
							"symbolSize": 25,
							"x": -250,
							"y": 50,
							"category": 4
						},
						{
							"id": "5",
							"name": "Attribute",
							"symbolSize": 30,
							"x": -320,
							"y": 100,
							"category": 5
						},
						{
							"id": "6",
							"name": "Class",
							"symbolSize": 80,
							"x": -260,
							"y": 85,
							"category": 6
						},
						{
							"id": "7",
							"name": "Inherit",
							"symbolSize": 30,
							"x": -200,
							"y": 100,
							"category": 7
						},
						{
							"id": "8",
							"name": "Method",
							"symbolSize": 70,
							"x": -250,
							"y": 130,
							"category": 8
						},
						{
							"id": "9",
							"name": "Override",
							"symbolSize": 30,
							"x": -230,
							"y": 120,
							"category": 9
						},
						{
							"id": "10",
							"name": "Call",
							"symbolSize": 20,
							"x": -240,
							"y": 150,
							"category": 10
						}
						],
						links: [
						{
							"source": "0",
							"target": "1"
						},
						{
							"source": "1",
							"target": "2"
						},
						{
							"source": "2",
							"target": "3"
						},
						{
							"source": "3",
							"target": "4"
						},
						{
							"source": "3",
							"target": "6"
						},
						{
							"source": "4",
							"target": "6"
						},
						{
							"source": "5",
							"target": "6"
						},
						{
							"source": "7",
							"target": "6"
						},
						{
							"source": "6",
							"target": "7"
						},
						{
							"source": "6",
							"target": "8"
						},
						{
							"source": "8",
							"target": "9"
						},
						{
							"source": "9",
							"target": "8"
						},
						{
							"source": "8",
							"target": "10"
						},
						{
							"source": "10",
							"target": "8"
						}
						],
						categories: [
						{"name": "A"},
						{"name": "B"},
						{"name": "C"},
						{"name": "D"},
						{"name": "E"},
						{"name": "F"},
						{"name": "G"},
						{"name": "H"},
						{"name": "I"},
						{"name": "J"}
						]
					}
					]
				}
			}
		}
	}
</script>

<style>
</style>
