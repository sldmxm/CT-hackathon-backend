import styles from './Board.module.css';

import { columnTitle } from '../../../helpers/static';
import { ColumnBoardContainer } from '../../ColumnBoard/container';

export function VacancyBoard() {
  const isHidden = true;

  return (
    <section className={styles.board}>
      {columnTitle.map((title, index) => (
        <ColumnBoardContainer
          key={index}
          title={title}
          isHidden={isHidden}
          columnPosition={index}
        />
      ))}
    </section>
  );
}
