import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import OriginalViewer from './OriginalViewer.vue'
import MapSheet from './MapSheet.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('MapSheet', MapSheet)
  },
  Layout: () => h(DefaultTheme.Layout, null, {
    'doc-after': () => h(OriginalViewer),
  }),
}
