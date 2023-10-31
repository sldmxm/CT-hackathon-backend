import { Outlet } from 'react-router-dom';

import { Header } from './Header';
import styles from './layout.module.css';
import { Sidebar } from './Sidebar';

export function Layout() {
  return (
    <div className={styles.root}>
      <Header className={styles.header} />
      <Sidebar className={styles.sidebar} />
      <main className={styles.content}>
        <Outlet />
      </main>
    </div>
  );
}
