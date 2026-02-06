import { useUser } from '@clerk/clerk-react';

export default function Avatar({ src, alt, size = 'md', className = '' }) {
    const { user, isLoaded } = useUser();

    const sizes = {
        sm: 'w-7 h-7 text-[10px]',
        md: 'w-8 h-8 text-[11px]',
        lg: 'w-10 h-10 text-[13px]',
    };

    // Determine name and image source
    // Priority: Prop > Clerk User > Fallback
    const name = alt || (isLoaded && user?.fullName) || 'User';
    const avatarSrc = src || (isLoaded && user?.imageUrl);

    // Calculate initials
    const initials = name
        ? name.split(' ').map(n => n[0]).join('').slice(0, 2).toUpperCase()
        : 'U';

    return (
        <div
            className={`
        ${sizes[size]} rounded-full overflow-hidden
        bg-[var(--bg-secondary)]
        flex items-center justify-center text-[var(--text-secondary)] font-medium
        ring-1 ring-[var(--border-color)]
        ${className}
      `}
        >
            {avatarSrc ? (
                <img src={avatarSrc} alt={name} className="w-full h-full object-cover" />
            ) : (
                <span>{initials}</span>
            )}
        </div>
    );
}
