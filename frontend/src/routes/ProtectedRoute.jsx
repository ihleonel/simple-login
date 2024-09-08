import { Redirect } from "wouter"

// eslint-disable-next-line react/prop-types
export default function ProtectedRoute({ component: Component }) {
  const isAuthenticated = true

  return isAuthenticated ? <Component /> : <Redirect to="/login" />
}
