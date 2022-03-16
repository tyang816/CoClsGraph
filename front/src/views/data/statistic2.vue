<template>
	<el-main>
		<el-alert title="各种数据的平均长度" type="success" style="margin-bottom:20px;"></el-alert>
		<el-row :gutter="15">
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="方法调用函数平均值" value="9.82" description="一个目标方法连接几个函数" tips="本项目中计算得到的数值" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="方法名平均长度" value="2.9" description="函数名的平均长度" tips="本项目中计算得到的数值" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="方法平均长度" value="130.7" description="函数的平均长度" tips="本项目中计算得到的数值" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="注释平均长度" value="19.1" description="注释的平均长度" tips="本项目中计算得到的数值" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
		</el-row>
		<el-row :gutter="15">
			<el-col :lg="24">
				<el-card shadow="never">
					<scEcharts height="300px" :option="option"></scEcharts>
				</el-card>
			</el-col>
		</el-row>
	</el-main>
</template>

<script>
	import scEcharts from '@/components/scEcharts';
	import scStatistic from '@/components/scStatistic';

	export default {
		name: 'statistic2',
		components: {
			scEcharts,
			scStatistic
		},
		data() {
			return {
				option: {
					title: {
						text: '平均统计值',
						subtext: '平均统计值折线图',
					},
					grid: {
						top: '80px'
					},
					tooltip: {
						trigger: 'axis'
					},
					xAxis: {
						type: 'category',
						data: ['方法调用函数平均值', '方法名平均长度', '方法平均长度', '注释平均长度']
					},
					yAxis: {
						type: 'value'
					},
					series: [{
						data: [9.82, 2.9, 130.7, 19.1],
						type: 'line',
					},]
				},
				

			}
		}
	}
</script>

<style>
</style>
