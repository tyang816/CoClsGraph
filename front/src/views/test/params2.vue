<template>
	<el-main>
		<el-alert title="这里展示了一些实验的发现~" type="success" style="margin-bottom:20px;"></el-alert>
		<el-row :gutter="15">
			<el-col :lg="24">
				<el-card shadow="never">
					<scEcharts height="400px" :option="option3"></scEcharts>
				</el-card>
			</el-col>
		</el-row>
		<el-row :gutter="15">
			<el-col :lg="24">
				<el-card shadow="never">
					<sc-statistic title="有趣发现1" value="复制概率较高的原因应该是来源于其上下文特征较多，注意力机制可以更好的关注目标及其关联函数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
		</el-row>
		<el-row :gutter="15">
			<el-col :lg="24">
				<el-card shadow="never">
					<scEcharts height="400px" :option="option4"></scEcharts>
				</el-card>
			</el-col>
		</el-row>
		<el-row :gutter="15">
			<el-col :lg="24">
				<el-card shadow="never">
					<sc-statistic title="有趣发现2" value="代码编写人员更偏向于写相似的，简单快捷的注释，说明程序员其实并不是排斥写注释，
					而是不希望写冗余，无意义的注释。但更有意思的是，在这种想法下，写出来的注释又是多是无意义的。因此后续可以考虑在
					注释文本问题上进行研究" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
		</el-row>
	</el-main>
</template>

<script>
	import scEcharts from '@/components/scEcharts';
	import scStatistic from '@/components/scStatistic';

	/**
	 * 引入组件 @/components/scEcharts
	 * 组件内部会自动加载主题 @/components/scEcharts/echarts-theme-T.js
	 * 支持props包括 height，width，option
	 * 组件export百度Echarts所有方法，使用方式: new scEcharts[fun]
	 */

	export default {
		name: 'parans2',
		components: {
			scEcharts,
			scStatistic
		},
		data() {
			return {
				option3: {
					title: {
						text: '词元源码复制概率',
						subtext: '从函数中直接复制到注释的概率',
					},
					tooltip: {
						trigger: 'item'
					},
					series: [
						{
							name: '复制概率',
							type: 'pie',
							radius: ['40%', '70%'],
							center: ['50%', '60%'],
							label: false,
							data: [
								{value: 19.4, name: '直接复制（百分比）'},
								{value: 80.6, name: '预测结果（百分比）'}
							]
						}
					]
				},
				option4: {
					title: {
						text: '注释分析',
						subtext: '注释的情况小结',
					},
					tooltip: {
						trigger: 'item'
					},
					radar: {
						radius: 100,
						center: ['50%', '55%'],
						indicator: [
							{ name: '相似注释', max: 100},
							{ name: '短文本注释', max: 100},
							{ name: '长文本注释', max: 100},
							{ name: '不写注释', max: 100},
							{ name: '低质量注释', max: 100},
							{ name: '高质量注释', max: 100}
						]
					},
					series: [{
						name: "注释情况",
						type: 'radar',
						areaStyle: {},
						data: [
							{
								value: [82, 66, 30, 73, 42, 14],
							}
						]
					}]
				}
			}
		}
	}
</script>

<style>
</style>
