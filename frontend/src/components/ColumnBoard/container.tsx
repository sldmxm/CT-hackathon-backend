import { useDrop } from 'react-dnd';

import { ColumnBoard } from './ui/component';

import { CandidateProps } from '../../interfaces/board.interface';
import { ColumnBoardProps } from '../../interfaces/column.interface';
import { selectBoardModule } from '../../redux-store/features/board/selector';

import { moveCandidate } from '../../redux-store/features/board/slice';
import { patchCandidateInfo } from '../../redux-store/features/board/thunk/patchCandidateInfo';
import { useAppSelector, useAppDispatch } from '../../redux-store/store';

export function ColumnBoardContainer({
  title,
  columnPosition,
  isHidden,
}: ColumnBoardProps) {
  const board = useAppSelector(selectBoardModule);
  const dispatch = useAppDispatch();
  const [, dropTarget] = useDrop({
    accept: 'candidate',
    drop: (item: CandidateProps) => {
      handleMoveItem(item);
    },
  });

  const handleMoveItem = (item: CandidateProps) => {
    dispatch(
      moveCandidate({
        id: item.id,
        position: columnPosition,
      })
    );
    dispatch(
      patchCandidateInfo({
        vacancyId: board[0].id,
        candidateId: item.id,
        position: columnPosition + 1,
      })
    );
  };

  const filteredCandidates = board[0].candidates.filter(
    ({ kanban_position }) => +kanban_position === columnPosition
  );

  return (
    <ColumnBoard
      title={title}
      dropRef={dropTarget}
      isHidden={isHidden}
      countCandidates={filteredCandidates.length}
      candidates={filteredCandidates}
      columnPosition={columnPosition}
    />
  );
}
