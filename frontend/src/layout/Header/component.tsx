import cn from 'classnames';

import styles from './header.module.css';

import { Account } from '../../components/Account';
import { Search } from '../../components/ui';

export function Header({ className }: { className: string }): JSX.Element {
  return (
    <header className={cn(className, styles.header)}>
      <div className={styles.container}>
        <Search />
        <Account />
      </div>
    </header>
  );
}
