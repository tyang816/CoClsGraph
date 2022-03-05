<template>
	<el-card shadow="hover" header="欢迎">
		<div class="welcome">
			<div class="logo">
				<img src="img/logo.png">
				<h2>欢迎体验 CoDesc</h2>
				<br>
				<br>
			</div>
		</div>
	</el-card>
</template>

<script>
	export default {
		title: "欢迎",
		icon: "el-icon-present",
		description: "",
		data() {
			return {

			}
		},
		methods: {

		}
	}
</script>

<style scoped>
	.welcome {}
	.welcome .logo {text-align: center;}
	.welcome .logo img {vertical-align: bottom;width: 140px;height: 100px;margin-bottom: 20px;}
	.welcome .logo h2 {font-size: 30px;font-weight: normal;display: flex;align-items: center;justify-content: center;}

</style>
