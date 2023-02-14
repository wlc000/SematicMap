<script setup lang="ts">
import {Ref, ref, shallowRef, triggerRef} from 'vue'

export interface User {
  name: string;
  count: Ref<number>;
}

defineProps<{ msg: string }>()

const count: Ref<number> = ref<number>(0)
const user: User = {
  name: "kkk",
  count: ref(4),
};

let message: Ref<User> = shallowRef({
  name: "111",
  count: shallowRef(3)
})

const changeMsg = (msg: Ref<User>) => {
  user.count.value++;
  msg.value = {
    name: "222",
    count: ref(5)
  }
  console.log(msg.value)
  triggerRef(msg)
}

</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <a-space>
      <a-button @click="count++">count is {{ count }}</a-button>
      <a-button @click="user['count'].value++">user[count] is {{ user["count"] }}</a-button>
      <a-button @click="changeMsg">{{ message["name"] }}</a-button>
    </a-space>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
  </div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
    >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/johnsoncodehk/volar" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
