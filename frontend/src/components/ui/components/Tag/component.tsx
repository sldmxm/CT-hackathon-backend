import { Typography } from '@mui/material';

import styles from './Tag.module.css';

type TTag = {
  text: string;
  style?: 'solid' | 'stroke';
  id?: number;
};

export const Tag = ({ text }: TTag): JSX.Element => {
  return (
    <div className={styles.tag}>
      <Typography variant='body2' className={styles['tag__text']}>
        {text}
      </Typography>
    </div>
  );
};
