import { RootState } from '../../store';

export const selectBoardModule = (state: RootState) => state.board.board;
