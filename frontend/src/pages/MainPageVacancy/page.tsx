import React from 'react';

import styles from './card.module.css';

import { CardListVacancyContainer } from '../../components/CardListVacancy';

import { CustomNavigateButton } from '../../components/ui';

const labels: string[] = ['Все', 'Активные', 'Архивные'];

export function MainPageVacancy(): JSX.Element {
  const [value, setValue] = React.useState(0);

  const handleChange = (_event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  return (
    <section>
      <h2 className={styles.Title}>Вакансии</h2>
      <CustomNavigateButton
        value={value}
        onChange={handleChange}
        labels={labels}
      />
      <CardListVacancyContainer value={value} />
    </section>
  );
}
