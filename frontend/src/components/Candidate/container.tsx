import { useDrag } from 'react-dnd';

import { Candidate } from './ui/component';

import { CandidateProps } from '../../interfaces/board.interface';

export function CandidateContainer({
  columnPosition,
  candidate,
}: {
  columnPosition: number;
  candidate: CandidateProps;
}) {
  const [{ isDrag }, dragRef] = useDrag({
    type: 'candidate',
    item: candidate,
    collect: (monitor) => ({
      isDrag: monitor.isDragging(),
    }),
  });

  return (
    !isDrag && (
      <Candidate
        columnPosition={columnPosition}
        dragRef={dragRef}
        candidate={candidate}
      />
    )
  );
}
