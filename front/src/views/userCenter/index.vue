<template>
	<el-main>
		<el-row :gutter="15">
			<el-col :lg="8">
				<el-card shadow="never">
					<div class="user-info">
						<div class="user-info-top">
							<el-avatar :size="80" src="img/avatar.jpg"></el-avatar>
							<h2>{{ form.name||'-' }}</h2>
							<p>{{ form.about||'无签名' }}</p>
							<el-button type="primary" round icon="el-icon-collection-tag" size="large">Administrator</el-button>
						</div>
						<div class="user-info-main">
							<ul>
								<li><label><el-icon><el-icon-user /></el-icon></label><span>ty_ang@163.com</span></li>
								<li><label><el-icon><el-icon-male /></el-icon></label><span>男</span></li>
								<li><label><el-icon><el-icon-location /></el-icon></label><span>中国/上海/徐汇</span></li>
								<li><label><el-icon><el-icon-office-building /></el-icon></label><span>华东理工大学</span></li>
								<li><label><el-icon><el-icon-coin /></el-icon></label><span>超级管理员</span></li>
							</ul>
						</div>
					</div>
				</el-card>
			</el-col>
			<el-col :lg="16">
				<el-card shadow="never">
					<el-tabs tab-position="top">
						<el-tab-pane :label="$t('user.info')">
							<el-form ref="form" :model="form" label-width="80px" style="width: 460px;margin-top:20px;">
								<el-form-item label="账号">
									<el-input v-model="form.user" disabled></el-input>
									<div class="el-form-item-msg">账号信息用于登录，系统不允许修改</div>
								</el-form-item>
								<el-form-item label="姓名">
									<el-input v-model="form.name"></el-input>
								</el-form-item>
								<el-form-item label="性别">
									<el-select v-model="form.sex" placeholder="请选择">
										<el-option label="保密" value="0"></el-option>
										<el-option label="男" value="1"></el-option>
										<el-option label="女" value="2"></el-option>
									</el-select>
								</el-form-item>
								<el-form-item label="个性签名">
									<el-input v-model="form.about" type="textarea"></el-input>
								</el-form-item>
								<el-form-item>
									<el-button type="primary">保存</el-button>
								</el-form-item>
							</el-form>
						</el-tab-pane>
						<el-tab-pane :label="$t('user.settings')">
							<el-form ref="form" :model="form" label-width="120px" style="margin-top:20px;">
								<el-form-item :label="$t('user.nightmode')">
									<el-switch v-model="config.theme" active-value="dark" inactive-value="default" inline-prompt active-icon="el-icon-moon" inactive-icon="el-icon-sunny"></el-switch>
									<div class="el-form-item-msg">{{ $t('user.nightmode_msg') }}</div>
								</el-form-item>
								<el-form-item label="主题颜色">
									<el-color-picker v-model="config.colorPrimary" :predefine="colorList">></el-color-picker>
								</el-form-item>
								<el-form-item :label="$t('user.language')">
									<el-select v-model="config.lang">
										<el-option label="简体中文" value="zh-cn"></el-option>
										<el-option label="English" value="en"></el-option>
										<el-option label="日本語" value="ja"></el-option>
									</el-select>
									<div class="el-form-item-msg">{{ $t('user.language_msg') }}</div>
								</el-form-item>
							</el-form>
						</el-tab-pane>
					</el-tabs>
				</el-card>
			</el-col>
		</el-row>
	</el-main>
</template>

<script>
	import colorTool from '@/utils/color'

	export default {
		name: 'userCenter',
		data() {
			return {
				form: {
					user: "ty_ang@163.com",
					name: "tyang",
					sex: "1",
					about: "正所谓富贵险中求"
				},
				colorList: ['#409EFF', '#009688', '#536dfe', '#ff5c93', '#c62f2f', '#fd726d'],
				config: {
					lang: this.$TOOL.data.get('APP_LANG') || this.$CONFIG.LANG,
					theme: this.$TOOL.data.get('APP_THEME') || 'default',
					colorPrimary: this.$TOOL.data.get('APP_COLOR') || this.$CONFIG.COLOR || '#409EFF'
				}
			}
		},
		watch:{
			'config.theme'(val){
				document.body.setAttribute('data-theme', val)
				this.$TOOL.data.set("APP_THEME", val);
			},
			'config.lang'(val){
				this.$i18n.locale = val
				this.$TOOL.data.set("APP_LANG", val);
			},
			'config.colorPrimary'(val){
				document.documentElement.style.setProperty('--el-color-primary', val);
				for (let i = 1; i <= 9; i++) {
					document.documentElement.style.setProperty(`--el-color-primary-light-${i}`, colorTool.lighten(val,i/10));
				}
				document.documentElement.style.setProperty(`--el-color-primary-darken-1`, colorTool.darken(val,0.1));
				this.$TOOL.data.set("APP_COLOR", val);
			}
		},
		//路由跳转进来 判断from是否有特殊标识做特殊处理
		beforeRouteEnter (to, from, next){
			next((vm)=>{
				if(from.is){
					//删除特殊标识，防止标签刷新重复执行
					delete from.is
					//执行特殊方法
					vm.$alert('路由跳转过来后含有特殊标识，做特殊处理', '提示', {
						type: 'success',
						center: true
					}).then(() => {}).catch(() => {})
				}
			})
		},
		methods: {

		}
	}
</script>

<style scoped>
	.el-card {margin-bottom:15px;}
	.activity-item {font-size: 13px;color: #999;display: flex;align-items: center;}
	.activity-item label {color: #333;margin-right:10px;}
	.activity-item .el-avatar {margin-right:10px;}
	.activity-item .el-tag {margin-right:10px;}

	[data-theme='dark'] .user-info-bottom {border-color: var(--el-border-color-base);}
	[data-theme='dark'] .activity-item label {color: #999;}
</style>
