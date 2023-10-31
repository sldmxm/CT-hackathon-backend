import styles from './BulletList.module.css';

interface BulletListProps {
  items: string[];
  withLabel?: boolean;
}

export function BulletList({ items }: BulletListProps) {
  return (
    <ul className={styles.list}>
      {items.map((item, index) => (
        <li className={styles.item} key={index}>
          {item}
        </li>
      ))}
    </ul>
  );
}
