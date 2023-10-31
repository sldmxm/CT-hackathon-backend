import cn from 'classnames';
import React from 'react';

import styles from './Badge.module.css';

export type ViewVariant =
  | 'Кандидаты'
  | 'Тестовое'
  | 'Собеседование'
  | 'Офер'
  | 'Отказ'
  | 'Резерв';

interface CustomBadgeProps {
  viewVariant: ViewVariant;
  children: React.ReactNode;
  className?: string;
}

export function CustomBadge({
  children,
  className,
  viewVariant,
}: CustomBadgeProps) {
  return (
    <div
      className={cn(styles.badge, className, {
        [styles.candidates]: viewVariant === 'Кандидаты',
        [styles.test]: viewVariant === 'Тестовое',
        [styles.interview]: viewVariant === 'Собеседование',
        [styles.offer]: viewVariant === 'Офер',
        [styles.refusal]: viewVariant === 'Отказ',
        [styles.reserve]: viewVariant === 'Резерв',
      })}
    >
      <span>{children}</span>
    </div>
  );
}
