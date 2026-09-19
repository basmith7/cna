import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import OriginalViewer from './OriginalViewer.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, {
    'doc-after': () => h(OriginalViewer),
  }),
}
