import { DndProvider } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';

import { VacancyBoard } from './ui/component';

export function VacancyBoardContainer() {
  return (
    <DndProvider backend={HTML5Backend}>
      <VacancyBoard />
    </DndProvider>
  );
}
