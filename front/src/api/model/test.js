import http from "@/utils/request"

export default {
	base: {
		url: `http://180.76.168.236:5000/base`,
		name: "获取目标函数与摘要",
		post: async function(data={}){
			return await http.post(this.url, data);
		}
	},
    class2base: {
		url: `http://180.76.168.236:5000/class2base`,
		name: "获取上下文函数",
		post: async function(data={}){
			return await http.post(this.url, data);
		}
	},
	relateshow: {
		url: `http://180.76.168.236:5000/relateshow`,
		name: "获取一个仓库关系图",
		post: async function(data={}){
			return await http.post(this.url, data);
		}
	}
}