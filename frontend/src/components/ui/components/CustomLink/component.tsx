import { NavLink, NavLinkProps, useLocation } from 'react-router-dom';

import styles from './CustomLink.module.css';

interface Route {
  path: string;
  icon?: {
    active: () => JSX.Element;
    unactive: () => JSX.Element;
  };
}

interface CustomLinkProps extends NavLinkProps {
  route: Route;
}

export function CustomLink({ route, ...props }: CustomLinkProps) {
  const location = useLocation();
  const Icon =
    location.pathname === props.to ? route.icon!.active : route.icon!.unactive;
  return (
    <NavLink {...props} className={styles.root}>
      {route.icon && (
        <div className={styles.icon}>
          <Icon />
        </div>
      )}
    </NavLink>
  );
}
