<template>
  <el-main>
    <el-alert
      title="本接龙对比工具仅供华理信息学院18级在校生核酸接龙对比名单使用！"
      type="warning"
      style="margin-bottom: 20px"
    ></el-alert>
		<el-card shadow="never" header="请在这里选择班级" style="margin-top: 15px;">
        <el-select v-model="value" placeholder="请选择班级">
          <el-option-group v-for="group in options" :key="group.label" :label="group.label">
            <el-option v-for="item in group.options" :key="item.value" :label="item.label" :value="item.value"/>
          </el-option-group>
        </el-select>
		</el-card>
    <el-card shadow="never" header="请在这里输入接龙内容" style="margin-top: 15px;">
        <el-input
          v-model="textarea"
          :autosize="{ minRows: 5, maxRows: 20 }"
          type="textarea"
          placeholder="请输入接龙信息"
        />
		<el-button type="primary" @click="contra" style="margin: 10px 0px">开始对比</el-button>
	</el-card>
	<el-card shadow="never" header="结果1" style="margin-top: 15px;">
			<el-input type="textarea" :rows="2" v-model="ans1"></el-input>
			<el-button v-copy="ans1" type="primary" style="margin-top: 15px;">复制</el-button>
		</el-card>
	<el-card shadow="never" header="结果2" style="margin-top: 15px;">
		<el-input type="textarea" :autosize="{ minRows: 5, maxRows: 20 }" v-model="ans2"></el-input>
		<el-button v-copy="ans2" type="primary" style="margin-top: 15px;">复制</el-button>
	</el-card>
  </el-main>
</template>

<script>
import scStatistic from "@/components/scStatistic";
import scEcharts from "@/components/scEcharts";
import { ref } from "vue";

export default {
  name: "jielong",
  components: {
    scStatistic,
    scEcharts,
  },
  data() {
    return {
      textarea: ref(""),
	  value: ref(''),
      options: [
        {
          label: "自动化",
          options: [
            {
              value: "动181",
              label: "动181",
            },
            {
              value: "动182",
              label: "动182",
            },
			{
              value: "动183",
              label: "动183",
            }
          ],
        },
        {
          label: "测仪",
          options: [
            {
              value: "测仪181",
              label: "测仪181",
            },
            {
              value: "测仪182",
              label: "测仪182",
            }
          ],
        },
		{
          label: "信工",
          options: [
            {
              value: "信工181",
              label: "信工181",
            },
            {
              value: "信工182",
              label: "信工182",
            },
			{
              value: "信工183",
              label: "信工183",
            }
          ],
        },
		{
          label: "计算机",
          options: [
            {
              value: "计181",
              label: "计181",
            },
            {
              value: "计182",
              label: "计182",
            },
			{
              value: "计183",
              label: "计183",
            }
          ],
        },
		{
          label: "软件工程",
          options: [
            {
              value: "软件181",
              label: "软件181",
            },
            {
              value: "软件182",
              label: "软件182",
            }
          ],
        },
      ],
	  ans1: ref(''),
	  ans2: ref(''),
	  copyText: '测试复制内容'
    };
  },
  mounted() {},
  methods: {
	  async contra(){
		var query = {
		  "clazz": this.value, 'content': this.textarea
		}
		var res = await this.$API.common.jielong.post(query)
		this.ans1 = res.ans1
		this.ans2 = res.ans2
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
