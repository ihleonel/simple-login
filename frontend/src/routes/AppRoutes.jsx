import { Switch, Route } from 'wouter'
import Home from '../pages/Home'
import Dashboard from '../pages/Dashboard'
import Login from '../pages/Login'
import ProtectedRoute from './ProtectedRoute'
export default function AppRoutes() {
  return (
    <Switch>
      <Route path="/" component={Home} />
      <Route path="/login" component={Login} />

      <ProtectedRoute path="/dashboard" component={Dashboard} />

      <Route>This is rendered when nothing above has matched</Route>
    </Switch>
  )
}
