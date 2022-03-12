<template>
	<el-main>
		<el-alert title="本图数据来源于GitHub开源仓库，经过大量清洗操作后展示！" type="success" style="margin-bottom:20px;"></el-alert>
		<el-row :gutter="15">
			<el-col :lg="24">
				<el-card shadow="never">
					<el-result
						icon="success"
						title="成功预测！预测结果如下：👇"
						:sub-title="summary"
					>	
					</el-result>
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
		name: 'autocode-summary',
		components: {
			scEcharts
		},
		data() {
			return {
				summary: this.$TOOL.data.get('SUMMARY')
				
			}
		}
	}
</script>

<style>
</style>
