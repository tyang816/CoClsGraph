<template>
	<el-main>
		<el-alert title="这里展示项目所用到的实验参数！" type="success" style="margin-bottom:20px;"></el-alert>
		<el-row :gutter="15">
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="max_node_num" value="10" description="图最大节点数" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="max_com_len" value="30" description="注释最大长度" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="max_code_len" value="100" description="代码最大长度" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="batch_size" value="20" description="批量大小" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="com_vocab_size" value="27008" description="注释词库大小" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="code_vocab_size" value="141204" description="代码词库大小" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="embed_size" value="128" description="嵌入层维度" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="hidden_size" value="128" description="隐藏层维度" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="gat_input_size" value="256" description="GAT输入维度" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="gat_hidden_size" value="128" description="GAT隐藏层维度" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="gat_dropout" value="0.1" description="GAT丢弃率" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
		</el-row>
		<el-alert title="这里展示项目所用到的实验数据量！" type="success" style="margin-bottom:20px;"></el-alert>
		<el-row :gutter="15">
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="train_num" value="276464" description="训练数据" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="test_num" value="34559" description="测试数据" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			<el-col :lg="6">
				<el-card shadow="never">
					<sc-statistic title="valid_num" value="34558" description="验证数据" tips="实验参数" groupSeparator></sc-statistic>
				</el-card>
			</el-col>
			
		</el-row>
	</el-main>
</template>

<script>
	import scStatistic from '@/components/scStatistic';
	import scEcharts from '@/components/scEcharts';

	export default {
		name: 'params',
		components: {
			scStatistic,
			scEcharts
		},
		data() {
			return {
				
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
