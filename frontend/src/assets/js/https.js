const apiMethods = {
  methods: {
    apiPost(url, data) {
      return new Promise((resolve, reject) => {
        axios.post(url, data).then((response) => {
          resolve(response.data)
        }).catch((response) => {
          resolve(response)
          bus.$message({
            message: '请求服务器失败，请检查网络',
            type: 'warning'
          })
        })
      })
    },
    apiPostExcel(url, data) {
      return new Promise((resolve, reject) => {
        axios.post(url, data).then((response) => {
          resolve(response.data)
        }).catch((response) => {
          resolve(response)
          bus.$message({
            message: '请求服务器失败，请检查网络',
            type: 'warning'
          })
        })
      })
    }
  }
}
export default apiMethods
