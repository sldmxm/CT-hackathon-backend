import styles from './candiadtes.module.css';

import { CandidateList } from '../../components/CandidateList/component';

export function CandidatesPage() {
  return (
    <section>
      <h2 className={styles.title}>Кандидаты</h2>
      <CandidateList />
    </section>
  );
}
