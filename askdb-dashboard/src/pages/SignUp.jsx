
import { SignUp } from "@clerk/clerk-react";

export default function SignUpPage() {
    return (
        <div className="min-h-screen bg-[var(--bg-primary)] flex items-center justify-center p-4">
            <SignUp routing="path" path="/sign-up" signInUrl="/login" />
        </div>
    );
}
