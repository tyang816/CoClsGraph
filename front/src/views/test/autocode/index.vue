<template>
	<router-view></router-view>
	<el-main>
		<el-alert title="请先点击`初始化`按钮初始化一个图数据！" type="success" style="margin-bottom:20px;">
			<el-button type="primary" @click="init">初始化</el-button>
		</el-alert>
		<el-row :gutter="15">
			<el-col :xl="6" :lg="6" :md="8" :sm="12" :xs="24" v-for="item in list" :key="item.title">
				<el-card shadow="hover" :body-style="{ padding: '0px' }" @click="click(item.url)">
					<div class="code-item">
						<div class="img" :style="{background: item.color}">
							<el-icon :style="`background-image: -webkit-linear-gradient(top left, #fff, ${item.color} 100px)`"><component :is="item.icon" /></el-icon>
						</div>
						<div class="title">
							<h2>{{item.title}}</h2>
							<h4>{{item.des}}</h4>
							<p><el-tag>{{item.ver}}</el-tag></p>
						</div>
					</div>
				</el-card>
			</el-col>
		</el-row>
	</el-main>
</template>

<script>
import { List } from 'echarts';
	export default {
		name: 'autocode',
		data() {
			return {
				list: [
					{
						title: "原始数据上下文图",
						des: "从数据库中初步读取目标类方法及其相关类",
						icon: "el-icon-finished",
						color: "#ccc",
						ver: "试用中",
						url: "/test/autocode/method"
					},
					{
						title: "简单清洗数据上下文图",
						des: "经过分词，消除驼峰命名，去除无意义词后的展示",
						icon: "el-icon-list",
						color: "#ccc",
						ver: "试用中",
						url: "/test/autocode/methodtoken"
					},
					{
						title: "代码摘要生成",
						des: "根据函数上下文及其信息通过神经网络生成最终的摘要",
						icon: "el-icon-documentChecked",
						color: "#ccc",
						ver: "试用中",
						url: "/test/autocode/summary"
					}
				]
			}
		},
		methods: {
			click(url){
				this.$router.push({
					path: url
				});
			},
			async init(){
				this.$TOOL.data.remove("BASE_DATA")
				this.$TOOL.data.remove("CLASS2BASE_DATA")
				this.$TOOL.data.remove("STEP1_DATA")
				this.$TOOL.data.remove("STEP1_LINK")
				this.$TOOL.data.remove("STEP2_DATA")
				this.$TOOL.data.remove("SUMMARY")
				var number = Math.round(Math.random()*39)+1
				var query = {
					"base_id": number
				}
				var base = await this.$API.test.base.post(query)
				var class2base = await this.$API.test.class2base.post(query)
				if(base.code == 200 && class2base.code == 200){
					this.$TOOL.data.set("BASE_DATA", base.data);
					this.$TOOL.data.set("CLASS2BASE_DATA", class2base.data);
				}
				
				var base_data = this.$TOOL.data.get('BASE_DATA')
				var class2base_data = this.$TOOL.data.get("CLASS2BASE_DATA")
				
				var step1_data = [
					{name: "目标方法", category: 0, desc: base_data['method']}
				]
				var base_method_token_format = []
				var base_method_token = eval(base_data['method_token'])
				for(var i=0;i<base_method_token.length;i++){
					if((i+1)%6 == 0){
						base_method_token_format.push('<br>')
					}
					base_method_token_format.push(base_method_token[i])
				}
				var step2_data = [
					{name: "目标方法", category: 0, desc: base_method_token_format}
				]
				var summary = eval(base_data['summary_token'])
				var sum_string = summary.join(' ')
				var step1_link = []
				for(var i=0;i<class2base_data.length;i++){
					step1_data.push({name: "关联类-"+i.toString(), category: 1, desc: class2base_data[i]['method']})
					var method_tokens = eval(class2base_data[i]['method_token'])
					var method_token_format = []
					for(var j=0;j<method_tokens.length;j++){
						if((j+1)%6 == 0){
							method_token_format.push('<br>')
						}
						method_token_format.push(method_tokens[j])
					}
					step2_data.push({name: "关联类-"+i.toString(), category: 1, desc: method_token_format.toString()})
					step1_link.push({source: "目标方法", target: "关联类-"+i.toString()})
				}
				this.$TOOL.data.set("STEP1_DATA", step1_data);
				this.$TOOL.data.set("STEP1_LINK", step1_link);
				this.$TOOL.data.set("STEP2_DATA", step2_data);
				this.$TOOL.data.set("SUMMARY", sum_string);
				var data1 = this.$TOOL.data.get('STEP1_DATA')
				var link1 = this.$TOOL.data.get('STEP1_LINK')
				var sumry = this.$TOOL.data.get('SUMMARY')
				
				console.log(data1)
				console.log(link1)
				console.log(sumry)
				
			}
		}
	}
</script>

<style scoped>
	.el-card {margin-bottom: 15px;}
	.code-item {cursor: pointer;}
	.code-item .img {width: 100%;height: 150px;background: #09f;display:flex;align-items: center;justify-content: center;}
	.code-item .img i {font-size: 100px;color: #fff;background-image: -webkit-linear-gradient(top left, #fff, #09f 100px);-webkit-background-clip: text;-webkit-text-fill-color: transparent;}
	.code-item .title {padding:15px;}
	.code-item .title h2 {font-size: 16px;}
	.code-item .title h4 {font-size: 12px;color: #999;font-weight: normal;margin-top: 5px;}
	.code-item .title p {margin-top: 15px;}
</style>
