import cn from 'classnames';

import styles from './sidebar.module.css';

import { CustomLink } from '../../components/ui';
import { navRoutes } from '../../helpers/nav.routes';

export function Sidebar({ className }: { className: string }) {
  return (
    <nav className={cn(className, styles.sidebar)}>
      <div className={styles.container}>
        {navRoutes.map((route, index) => (
          <CustomLink key={index} to={`/${route.path}`} route={route} />
        ))}
      </div>
    </nav>
  );
}
