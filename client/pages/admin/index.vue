<template>
  <div>
    <Header-admin></Header-admin>
    <div class="section bg-color-brown">
      <div class="container-fluid">
        <div class="row">
          <div class="col-md-2 col-4 bg-color-admin">
            <Left-admin> </Left-admin>
          </div>
          <div class="col-md-10 col-8">
            <div class="row">
              <div class="col-12 bg-white">
                <span style="font-size: 22px; font-weight: 600">Dashboard</span>
              </div>
              <div class="col-lg-3 col-md-6 col-12">
                <div class="user-adm user">
                  <div class="d-column">
                    <a href="">USERS</a>
                    <span>1</span>
                  </div>
                  <div>
                    <a href="">
                      <i class="far fa-user"></i>
                    </a>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-6 col-12">
                <div class="product-adm user">
                  <div class="d-column">
                    <NuxtLink to="/admin/products">PRODUCTS</NuxtLink>
                    <span>2</span>
                  </div>
                  <div>
                    <a href="">
                      <i class="fas fa-laptop"></i>
                    </a>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-6 col-12">
                <div class="order-adm user">
                  <div class="d-column">
                    <a href="/admin/orders">ORDERS</a>
                    <span>3</span>
                  </div>
                  <div>
                    <a href="">
                      <i class="fas fa-cart-arrow-down"></i>
                    </a>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-6 col-12">
                <div class="messages-adm user">
                  <div class="d-column">
                    <NuxtLink to="/admin/feedback">Feedback</NuxtLink>
                    <span>4</span>
                  </div>
                  <div>
                    <a href="">
                      <i class="fas fa-envelope-open-text"></i>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  async asyncData({ $axios }) {
    const orders = await $axios.$get('/adminorderview/')
    return { orders }
  },
  methods: {
    async changeorderstatus(OrderID, cancelorder = false) {
      if (cancelorder) {
        await this.$axios.delete('adminorderview/', {
          data: { orderid: OrderID },
        })
      }
      await this.$axios.post('adminorderview/', {
        orderid: OrderID,
      })
      this.$router.go()
    },
  },
}
</script>
