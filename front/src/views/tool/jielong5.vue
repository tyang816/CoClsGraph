<template>
  <el-main>
    <el-alert
      title="本接龙对比工具仅供华理信23舍5层在校生核酸接龙对比名单使用！"
      type="warning"
      style="margin-bottom: 20px"
    ></el-alert>
    <el-card shadow="never" header="请在这里输入23舍-5层接龙内容" style="margin-top: 15px;">
        <el-input
          v-model="textarea"
          :autosize="{ minRows: 5, maxRows: 20 }"
          type="textarea"
          placeholder="请输入23舍-5层接龙信息"
        />
		<el-button type="primary" @click="contra" style="margin: 10px 0px">开始对比</el-button>
	</el-card>
	<el-card shadow="never" header="结果" style="margin-top: 15px;">
			<el-input type="textarea" :rows="2" v-model="ans1"></el-input>
			<el-button v-copy="ans1" type="primary" style="margin-top: 15px;">复制</el-button>
		</el-card>
  </el-main>
</template>

<script>
import scStatistic from "@/components/scStatistic";
import scEcharts from "@/components/scEcharts";
import { ref } from "vue";

export default {
  name: "jielong5",
  components: {
    scStatistic,
    scEcharts,
  },
  data() {
    return {
      textarea: ref(""),
	  value: ref(''),
	  ans1: ref(''),
	  copyText: '测试复制内容'
    };
  },
  mounted() {},
  methods: {
	  async contra(){
		var query = {
		  'content': this.textarea
		}
		var res = await this.$API.common.jielong5.post(query)
		this.ans1 = res.ans1
	  }
  },
};
</script>

<style scoped>
.el-card {
  margin-bottom: 15px;
}
.up {
  color: #f56c6c;
  margin-left: 5px;
}
.down {
  color: #67c23a;
  margin-left: 5px;
}
</style>
