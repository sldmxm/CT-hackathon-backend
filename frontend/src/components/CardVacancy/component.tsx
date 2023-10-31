import { CardMedia, Typography, IconButton } from '@mui/material';

import styles from './card.module.css';

import img from './logoMock.png';

import { formatDate } from '../../helpers/utils';
import { Vacancy } from '../../interfaces/vacancy.interface';
import { CustomCard } from '../ui/components/CustomCard/component';
import { PanIcon } from '../ui/icons';

export function CardVacancy({
  vacancies,
}: {
  vacancies: Vacancy;
}): JSX.Element {
  return (
    <CustomCard>
      <div className={styles.Header}>
        <div className={styles.Company}>
          <CardMedia
            component='img'
            alt='Логотип'
            height='40'
            width='40'
            image={`${!vacancies.image ? img : vacancies.image}`}
            className={styles.img}
          />
          <div>
            <Typography variant='body2' className={styles.Name}>
              {vacancies.company}
            </Typography>
          </div>
        </div>
        <IconButton color='primary' className={styles.IconButton}>
          <PanIcon />
        </IconButton>
      </div>

      <div className={styles.info}>
        <p className={styles.Post}>{vacancies.specialty}</p>
        <p className={styles.PostDate}>
          Опубликована {formatDate(vacancies.updated_at)}
        </p>
      </div>
      <div className={styles.Tegs}>
        {vacancies.work_format.map((format, index) => (
          <div key={index} className={styles.Teg}>
            <Typography className={styles.TegText}>{format.name}</Typography>
          </div>
        ))}
      </div>
      <div className={styles.Status}>
        <figure
          className={`${
            vacancies.is_active
              ? styles.Point + ' ' + styles.Point_active
              : styles.Point + ' ' + styles.Point_disable
          }`}
        />
        <p className={styles.Text}>
          {vacancies.is_active ? 'активная' : 'Неактивная'}
        </p>
      </div>
    </CustomCard>
  );
}
