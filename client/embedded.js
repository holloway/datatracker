import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPersist from 'pinia-plugin-persist'
import Embedded from './Embedded.vue'

// Initialize store (Pinia)

window.pinia = window.pinia ?? createPinia()
pinia.use(piniaPersist)

// Mount App

const mountEls = document.querySelectorAll('div.vue-embed')
for (const mnt of mountEls) {
  const app = createApp(Embedded, {
    componentName: mnt.dataset.component,
    componentId: mnt.dataset.componentId
  })
  app.use(window.pinia)
  app.mount(mnt)
}
