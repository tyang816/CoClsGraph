import config from "@/config"
import http from "@/utils/request"

export default {
	jielong: {
		url: `http://127.0.0.1:5000/jielong`,
		name: "获取接龙对比",
		post: async function(data={}){
			return await http.post(this.url, data);
		}
	},
	jielong5: {
		url: `http://127.0.0.1:5000/jielong5`,
		name: "获取接龙5楼层对比",
		post: async function(data={}){
			return await http.post(this.url, data);
		}
	},
	upload: {
		url: `${config.API_URL}/upload`,
		name: "文件上传",
		post: async function(data, config={}){
			return await http.post(this.url, data, config);
		}
	},
	file: {
		menu: {
			url: `${config.API_URL}/file/menu`,
			name: "获取文件分类",
			get: async function(){
				return await http.get(this.url);
			}
		},
		list: {
			url: `${config.API_URL}/file/list`,
			name: "获取文件列表",
			get: async function(params){
				return await http.get(this.url, params);
			}
		}
	}
}
