import http from "@/utils/request"

export default {
	token: {
		url: `http://180.76.168.236:5000/token`,
		name: "登录获取TOKEN",
		post: async function(data={}){
			return await http.post(this.url, data);
		}
	}
}
