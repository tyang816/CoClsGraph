<template>
	<el-main>
		<el-row :gutter="15">
			<el-col :lg="24">
				<el-card shadow="never" class="aboutTop">
					<div class="aboutTop-info">
						<img src="img/logo.png">
						<h2>CoDesc</h2>
					</div>
				</el-card>
				<el-card shadow="never" header="deepDependencies">
					<el-descriptions border :column="3">
						<el-descriptions-item label="torch">1.10.1</el-descriptions-item>
						<el-descriptions-item label="torch-cluster">1.5.9</el-descriptions-item>
						<el-descriptions-item label="torch-geometric">2.0.3</el-descriptions-item>
						<el-descriptions-item label="torch-scatter">2.0.9</el-descriptions-item>
						<el-descriptions-item label="torch-sparse">0.6.12</el-descriptions-item>
						<el-descriptions-item label="torch-spline-conv">1.2.1</el-descriptions-item>
						<el-descriptions-item label="torchaudio">0.10.1</el-descriptions-item>
						<el-descriptions-item label="torchtext">0.11.0</el-descriptions-item>
						<el-descriptions-item label="torchvision">0.11.2</el-descriptions-item>
						<el-descriptions-item label="tornado">6.1</el-descriptions-item>
						<el-descriptions-item label="numpy">1.21.2</el-descriptions-item>
						<el-descriptions-item label="pandas">1.3.3</el-descriptions-item>
					</el-descriptions>
				</el-card>
				<el-card shadow="never" header="spider&backendDependencies">
					<el-descriptions border :column="3">
						<el-descriptions-item label="Scrapy">2.6.1</el-descriptions-item>
						<el-descriptions-item label="selenium">4.1.2</el-descriptions-item>
						<el-descriptions-item label="requests">2.26.0</el-descriptions-item>
						<el-descriptions-item label="requests-oauthlib">1.3.1</el-descriptions-item>
						<el-descriptions-item label="urllib3">1.26.7</el-descriptions-item>
						<el-descriptions-item label="Flask">2.0.3</el-descriptions-item>
						<el-descriptions-item label="Flask-SQLAlchemy">2.1</el-descriptions-item>
					</el-descriptions>
				</el-card>
				<el-card shadow="never" header="frontDependencies">
					<el-descriptions border :column="3">
						<el-descriptions-item v-for="(value, key) in data.dependencies" :key="key" :label="key">{{value}}</el-descriptions-item>
					</el-descriptions>
				</el-card>
				<el-card shadow="never" header="devDependencies">
					<el-descriptions border :column="3">
						<el-descriptions-item v-for="(value, key) in data.devDependencies" :key="key" :label="key">{{value}}</el-descriptions-item>
					</el-descriptions>
				</el-card>
			</el-col>
		</el-row>
	</el-main>
</template>

<script>
	import packageJson from '../../../package.json'

	export default {
		name: 'about',
		data() {
			return {
				data: packageJson
			}
		},
		mounted() {

		},
		methods: {

		}
	}
</script>

<style scoped>
	.aboutTop {border:0;background: linear-gradient(to right, #8E54E9, #4776E6);color: #fff;}
	.aboutTop-info {text-align: center}
	.aboutTop-info img {width: 100px;}
	.aboutTop-info h2 {font-size: 26px;margin-top: 15px;}
	.aboutTop-info p {font-size: 16px;margin-top: 10px;}
</style>
