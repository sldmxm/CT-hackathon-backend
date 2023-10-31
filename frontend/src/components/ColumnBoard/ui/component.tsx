import { Checkbox } from '@mui/material';
import cn from 'classnames';

import React from 'react';
import { ConnectDropTarget } from 'react-dnd';

import styles from './ColumnBoard.module.css';

import { CandidateProps } from '../../../interfaces/board.interface';
import { CandidateContainer } from '../../Candidate';
import { CustomBadge } from '../../ui';
import { ViewVariant } from '../../ui/components/Badge/component';

export function ColumnBoard({
  isHidden,
  countCandidates,
  title,
  candidates,
  columnPosition,
  dropRef,
}: {
  isHidden: boolean;
  countCandidates: number;
  title: ViewVariant;
  candidates: CandidateProps[];
  dropRef: ConnectDropTarget;
  columnPosition: number;
}) {
  const [activeColomnPosition, setIsActiveColomnPosition] = React.useState(-1);

  const handleChooseAllCandidates = (index: number) => {
    if (isHidden) {
      setIsActiveColomnPosition(activeColomnPosition === index ? -1 : index);
    } else {
      setIsActiveColomnPosition(-1);
    }
  };

  return (
    <div className={styles.column} ref={dropRef}>
      <div className={styles.columnInfo}>
        <Checkbox
          disabled={!countCandidates}
          onClick={() => handleChooseAllCandidates(columnPosition)}
          className={cn(styles.checkbox, {
            [styles.hidden]: !isHidden,
          })}
        />
        <h3 className={styles.title}>{title}</h3>
        <CustomBadge viewVariant={title} children={countCandidates} />
      </div>
      <div className={styles.candidateList}>
        {candidates.map((candidate) => (
          <CandidateContainer
            columnPosition={activeColomnPosition}
            key={candidate.id}
            candidate={candidate}
          />
        ))}
      </div>
    </div>
  );
}
