<template>
	<el-main>
		<el-alert title="这里展示项目所用到的所有数据的数值统计，给访问者对本人工作量以最直观的体验！" type="success" style="margin-bottom:20px;"></el-alert>
		<el-row :gutter="15">
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="repository" value="500" description="仓库数" tips="云服务器上存储数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="sourcedir" value="1358" description="源路径数" tips="云服务器上存储数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="package" value="8837" description="包数" tips="云服务器上存储数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="java" value="45702" description="java文件数" tips="云服务器上存储数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="import" value="120752" description="导入条数" tips="云服务器上存储数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="class" value="43900" description="类数" tips="云服务器上存储数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="method" value="320447" description="方法数" tips="云服务器上存储数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="inherit" value="39973" description="继承条数" tips="云服务器上存储数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
		</el-row>
		<el-row :gutter="15">
			<el-col :lg="24">
				<el-card shadow="never">
					<scEcharts height="500px" :option="option"></scEcharts>
				</el-card>
			</el-col>
		</el-row>
	</el-main>
</template>

<script>
	import scStatistic from '@/components/scStatistic';
	import scEcharts from '@/components/scEcharts';

	export default {
		name: 'statistic',
		components: {
			scStatistic,
			scEcharts
		},
		data() {
			return {
				trendValue2: -18.9,
				option: {
					title: {
						text: '数据统计柱状图',
						subtext: '统计各个类所对应的表的数据量',
					},
					grid: {
						top: '80px'
					},
					tooltip: {
						trigger: 'axis'
					},
					xAxis: {
						type: 'category',
						data: ['repository','sourcedir', 'package', 'java', 'import', 'class', 
								'method', 'inherit']
					},
					yAxis: {
						type: 'value'
					},
					series: [{
						data: [500, 1358, 8837, 45702, 120752, 43900, 320447, 39973],
						type: 'bar',
						barWidth: '15px',
					},
					]
				},
			}
		},
		mounted() {

		},
		methods: {

		}
	}
</script>

<style scoped>
	.el-card {margin-bottom: 15px;}
	.up {color: #F56C6C;margin-left: 5px;}
	.down {color: #67C23A;margin-left: 5px;}
</style>
