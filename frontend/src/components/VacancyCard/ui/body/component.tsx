/* eslint-disable @typescript-eslint/ban-ts-comment */
import { Button, CardContent, List, ListItem, Typography } from '@mui/material';

import { Link } from 'react-router-dom';

import { titles, matchHash } from '../../../../helpers/static';
import { Vacancy } from '../../../../interfaces/vacancy.interface';
import { CardContentWrapper } from '../../../ui';
import { BulletList } from '../../../ui/components/BulletList/component';
import styles from '../Ui.module.css';

export function VacancyCardBody({ vacancy }: { vacancy: Vacancy }) {
  function matchData(title: string, data: Vacancy) {
    const key = matchHash[title];
    //@ts-ignore
    const dataArray = data[key];

    if (Array.isArray(dataArray)) {
      if (key === 'hard_skill') {
        const components = dataArray.map((format, index) => (
          <div className={styles.teg} key={index}>
            <Typography className={styles.tegText}>{format.name}</Typography>
          </div>
        ));
        return <div className={styles.Tegs}>{components}</div>;
      } else {
        const components = dataArray.map((item, index) => (
          <ListItem sx={{ padding: 0, margin: 0 }} key={index}>
            <Typography
              variant='body1'
              sx={{
                fontSize: 16,
                fontStyle: 'normal',
                fontWeight: 400,
                lineHeight: '20px',
              }}
            >
              {item.name}
            </Typography>
          </ListItem>
        ));
        return <List sx={{ padding: 0, margin: 0 }}>{components}</List>;
      }
    }

    let content;

    if (key === 'description') {
      content = <BulletList items={dataArray.split('.')} />;
    } else {
      content = (
        <Typography
          sx={{
            fontSize: '16px',
            lineHeight: '20px',
          }}
        >
          {dataArray}
        </Typography>
      );
    }

    return <div>{content}</div>;
  }

  return (
    <CardContent
      sx={{
        display: 'flex',
        flexWrap: 'wrap',
        gap: '20px',
        padding: 0,
        transition: 'height 0.3s',
      }}
    >
      {titles.map((title, index) => {
        const matchResult = matchData(title, vacancy);
        return (
          <CardContentWrapper key={index} title={title}>
            {matchResult}
          </CardContentWrapper>
        );
      })}
      <CardContentWrapper title='Тестовое'>
        <Link to={'#'}>
          <Button
            sx={{
              fontSize: '14px',
              fontStyle: 'normal',
              fontWeight: 500,
              lineHeight: '20px',
              color: '#1D6BF3',
              padding: '0px',
              textTransform: 'none',
            }}
          >
            Выполнить тестовое
          </Button>
        </Link>
      </CardContentWrapper>
    </CardContent>
  );
}
