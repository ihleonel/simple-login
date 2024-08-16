import { Switch, Route } from 'wouter'
import Login from '../pages/Login'
import Home from '../pages/Home'
export default function AppRoutes() {
  return (
    <Switch>
      <Route path="/" component={Home} />
      <Route path="/login" component={Login} />
      <Route>This is rendered when nothing above has matched</Route>
    </Switch>
  )
}
