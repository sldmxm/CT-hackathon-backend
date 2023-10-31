import { Card, Collapse } from '@mui/material';

import React from 'react';

import { VacancyCardBody, VacancyCardHeader } from './ui';

import { Vacancy } from '../../interfaces/vacancy.interface';

export function VacancyCard({ vacancy }: { vacancy: Vacancy }) {
  const [expanded, setExpanded] = React.useState(false);
  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  return (
    <Card
      variant='outlined'
      sx={{
        border: 'none',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'flex-end',
        alignItems: 'flex-start',
        gap: '32px',
      }}
    >
      <VacancyCardHeader
        title={vacancy.title}
        image={vacancy.image}
        expanded={expanded}
        handleExpandClick={handleExpandClick}
      />
      <Collapse in={expanded} timeout='auto' unmountOnExit>
        <VacancyCardBody vacancy={vacancy} />
      </Collapse>
    </Card>
  );
}
