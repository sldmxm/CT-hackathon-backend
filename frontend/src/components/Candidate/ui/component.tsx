import { Avatar, CardHeader } from '@mui/material';
import { ConnectDragSource } from 'react-dnd';

import styles from './candidate.module.css';

import { CardProvider } from './card.provider';

import imgMock from './user-photo.png';

import { formatDate } from '../../../helpers/utils';
import { CandidateProps } from '../../../interfaces/board.interface';

export function Candidate({
  dragRef,
  candidate,
  columnPosition,
}: {
  dragRef: ConnectDragSource;
  candidate: CandidateProps;
  columnPosition: number;
}) {
  const isActive = columnPosition === +candidate.kanban_position;

  return (
    <div ref={!isActive ? dragRef : null} className={styles.container}>
      <CardProvider isActive={isActive}>
        <CardHeader
          sx={{ width: '100%', boxSizing: 'border-box', padding: '0' }}
          avatar={
            <Avatar
              aria-label='level'
              alt={`${candidate.student.first_name} ${candidate.student.last_name}`}
              src={
                !candidate.student.image
                  ? imgMock
                  : String(candidate.student.image)
              }
            />
          }
          title={
            <p
              className={styles.title}
            >{`${candidate.student.first_name} ${candidate.student.last_name}`}</p>
          }
        />
        <p className={styles.subtitle}>{formatDate(candidate.created_at)}</p>
      </CardProvider>
    </div>
  );
}
