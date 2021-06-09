package life.qbic.portal.sampletracking.components

import com.vaadin.shared.Position
import com.vaadin.ui.Notification
import com.vaadin.ui.themes.ValoTheme

class StyledNotification extends Notification {


    StyledNotification(String caption) {
        super(caption)
        setNotificationProperties()
    }

    StyledNotification(String caption, Type type) {
        super(caption, Type.HUMANIZED_MESSAGE)
        setNotificationProperties(type)
    }

    StyledNotification(String caption, String description) {
        super(caption, description, Type.HUMANIZED_MESSAGE)
        setNotificationProperties(Type.HUMANIZED_MESSAGE)
    }

    StyledNotification(String caption, String description, Type type) {
        super(caption, description, Type.HUMANIZED_MESSAGE)
        setNotificationProperties(type)
    }

    private setNotificationProperties(Type type) {
        this.setPosition(Position.MIDDLE_CENTER)
        switch (type) {
            case Type.WARNING_MESSAGE:
                this.setStyleName("${ValoTheme.NOTIFICATION_BAR} " +
                    "${ValoTheme.NOTIFICATION_WARNING} " +
                    "${ValoTheme.NOTIFICATION_CLOSABLE}")
                break
            case Type.ERROR_MESSAGE:
                this.setStyleName("${ValoTheme.NOTIFICATION_BAR} " +
                    "${ValoTheme.NOTIFICATION_FAILURE} " +
                    "${ValoTheme.NOTIFICATION_CLOSABLE}")
                break
            default:
                this.setStyleName("${ValoTheme.NOTIFICATION_BAR} " +
                    "${ValoTheme.NOTIFICATION_SUCCESS} " +
                    "${ValoTheme.NOTIFICATION_CLOSABLE}")
                break
        }
        this.setDelayMsec(5000)
    }
}
