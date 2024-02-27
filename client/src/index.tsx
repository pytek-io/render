import { main } from './app'
import { register_callbacks } from './callbacks'
register_callbacks()
import { register as register_react } from './libraries/html'
register_react()
import { register as register_antd } from './libraries/antd'
register_antd()
import { register as register_ant_icons } from './libraries/ant-icons'
register_ant_icons()
import { register as register_monaco } from './libraries/monaco'
register_monaco()
import { register as register_prism } from './libraries/prism'
register_prism()
import { register as register_rc_dock } from './libraries/rc-dock'
register_rc_dock()
import { register as register_ag_grid } from './libraries/ag-grid'
register_ag_grid()
import { register as register_plotly } from './libraries/plotly'
register_plotly()
import { register as register_spectacle } from './libraries/spectacle'
register_spectacle()
import { register as register_altair } from './libraries/altair'
register_altair()
import { register as register_bokeh } from './libraries/bokeh'
register_bokeh()
import { register as register_swiper } from './libraries/swiper'
register_swiper()
import { register as register_mantine } from './libraries/mantine'
register_mantine()
import { register as register_iconify } from './libraries/iconify'
register_iconify()
import { register as register_tabler_icons } from './libraries/tabler_icons'
register_tabler_icons()
import { register_mantine_prism } from './libraries/mantine_code_highlight'
register_mantine_prism()
main()