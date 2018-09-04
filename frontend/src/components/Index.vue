<template>
  <div>
    <el-button type="primary" round @click="handleShowCreate">增加书籍</el-button>
    <el-input v-model="search" placeholder="请输入内容" style="width: 200px"  @keyup.enter.native="handleSearch"/>
    <el-button type="primary" round @click="handleSearch">搜索</el-button>
    <el-table :data="booksData" height="250" border style="width: 600px; margin: 40px auto;"  v-loading="loading">
      <el-table-column
        prop="book_name"
        label="书名"
        align="center"
        width="200">
      </el-table-column>
      <el-table-column
        prop="book_price"
        label="价格"
        align="center"
        width="200">
      </el-table-column>
      <el-table-column label="操作" align="center">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleUpdate(scope.$index, scope.row)">编辑</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog title="修改书籍" :visible.sync="dialogUpdateVisible">
      <el-form :model="updateData">
        <el-form-item label="书籍名称">
          <el-input auto-complete="off" v-model="updateData.name"></el-input>
        </el-form-item>
        <el-form-item label="书籍价格">
          <el-input-number v-model="updateData.price" :precision="2" :step="0.01" :max="9999"></el-input-number>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="handleCancel('dialogUpdateVisible')">Cancel</el-button>
        <el-button type="primary" @click="handleConfirm('dialogUpdateVisible')">Submit</el-button>
      </div>
    </el-dialog>
    <el-dialog title="增加书籍" :visible.sync="dialogCreateVisible">
      <el-form :model="createData">
        <el-form-item label="书籍名称">
          <el-input auto-complete="off" v-model="createData.name"></el-input>
        </el-form-item>
        <el-form-item label="书籍价格">
          <el-input-number v-model="createData.price" :precision="2" :step="0.01" :max="9999"></el-input-number>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="handleCancel('dialogCreateVisible')">Cancel</el-button>
        <el-button type="primary" @click="handleCreate('dialogCreateVisible')">Submit</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'index',
  data () {
    return {
      search: '',
      booksData: [],
      oldData: {},
      updateData: {},
      createData: {
        name: '',
        price: 0
      },
      dialogUpdateVisible: false,
      dialogCreateVisible: false,
      loading: true
    }
  },
  methods: {
    handleShowCreate () {
      this.dialogCreateVisible = true
    },
    handleCreate () {
      if (this.createData.name === '') {
        this.$message.error('please input book name')
        return
      }
      if (this.createData.price === 0) {
        this.$message.error('please input book price')
        return
      }
      this.$axios.post('/create/', JSON.stringify(this.createData)).then(res => {
        if (res.data.code === 200) {
          this.$message.success(`create ${this.createData.name} success`)
          this.dialogCreateVisible = false
          this.handleRead()
        } else {
          this.$message.error("can't read books database")
        }
      })
      console.log(this.createData)
    },
    handleRead () {
      this.booksData = []
      this.$axios.get('/read').then(res => {
        this.loading = false
        if (res.data.code === 200) {
          let books = JSON.parse(res.data.data)
          for (let i in books) {
            books[i].fields.id = books[i].pk
            books[i].fields.book_price = Number(books[i].fields.book_price)
            this.booksData.push(books[i].fields)
          }
          console.log(this.booksData)
        } else {
          this.$message.console.error("can't read books database")
        }
      }).catch((res) => {
        console.log(res)
      })
    },
    handleUpdate (index, row) {
      this.dialogUpdateVisible = true
      this.updateData = Object.assign({}, {
        id: row.id,
        name: row.book_name,
        price: row.book_price,
        time: row.book_time
      })
      this.oldData = Object.assign({}, {
        id: row.id,
        name: row.book_name,
        price: row.book_price,
        time: row.book_time
      })
    },
    handleDelete (index, row) {
      this.$confirm(`are you sure to delete ${this.updateData.name} ?`, '', {
        confirmButtonText: 'submit',
        cancelButtonText: 'cancel',
        type: 'warning'
      }).then(() => {
        this.$axios.post('/delete/', JSON.stringify(row)).then(res => {
          if (res.data.code === 200) {
            this.$message.success(`delete ${this.updateData.name} success`)
            this.handleRead()
          } else {
            this.$message.error("can't read books database")
          }
        })
      }).catch(() => {
        this.$message.info('cancel delete')
      })
    },
    handleCancel (arg) {
      this.$message.info('cancel')
      this[arg] = false
    },
    handleConfirm (arg) {
      if (this.updateData.name === this.oldData.name && this.updateData.price === this.oldData.price) {
        this.$message.error('please update something or cancel')
        return
      }
      this[arg] = false
      this.$axios.post('/update/', JSON.stringify(this.updateData)).then(res => {
        if (res.data.code === 200) {
          this.$message.success(`update ${this.updateData.name} success`)
          this.handleRead()
        } else {
          this.$message.error("can't read books database")
        }
      })
    },
    handleSearch () {
      this.$axios.get('search', {
        params: {
          content: this.search
        }
      }).then(res => {
        if (res.data.code === 200) {
          if (res.data.data && JSON.parse(res.data.data).length > 0) {
            this.booksData = []
            let books = JSON.parse(res.data.data)
            for (let i in books) {
              let obj = {
                id: books[i].pk,
                book_name: books[i].fields.book_name,
                book_price: Number(books[i].fields.book_price),
                book_time: books[i].fields.book_time
              }
              this.booksData.push(obj)
            }
          } else {
            this.$message.error(`can't search contains of '${this.search}' in database`)
          }
        } else {
          this.$message.error(`can't search books in database`)
        }
      })
    }
  },
  mounted () {
    this.handleRead()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
